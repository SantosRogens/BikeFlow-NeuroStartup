"""Simulador BikeFlow (terminal). Execute após treinar o notebook.

Uso: python app.py --hora 17 --mes 6 --temperatura 25 --clima 1
"""
from pathlib import Path
import argparse
import pandas as pd
import joblib
import keras

BASE = Path(__file__).resolve().parent
FEATURES = ['season','mnth','hr','holiday','weekday','workingday','weathersit',
            'temp','atemp','hum','windspeed']

def prever(args):
    for caminho in ['bikeflow.keras','preprocessador.joblib','escala_alvo.joblib']:
        if not (BASE/'modelos'/caminho).exists():
            raise FileNotFoundError(f'Falta modelos/{caminho}. Execute o notebook primeiro.')
    modelo = keras.models.load_model(BASE/'modelos'/'bikeflow.keras')
    pre = joblib.load(BASE/'modelos'/'preprocessador.joblib')
    escala = joblib.load(BASE/'modelos'/'escala_alvo.joblib')
    dados = pd.DataFrame([{
        'season':args.estacao, 'mnth':args.mes, 'hr':args.hora,
        'holiday':int(args.feriado), 'weekday':args.dia_semana,
        'workingday':int(args.dia_util), 'weathersit':args.clima,
        'temp':(args.temperatura+8)/47,
        'atemp':(args.sensacao+16)/66,
        'hum':args.umidade/100,
        'windspeed':args.vento/67
    }],columns=FEATURES)
    X = pre.transform(dados).astype('float32')
    y = modelo.predict(X, verbose=0)
    return int(max(0, round(float(escala.inverse_transform(y)[0,0]))))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Estima bicicletas alugadas em uma hora com BikeFlow')
    parser.add_argument('--hora',type=int,default=17,choices=range(24),metavar='0..23')
    parser.add_argument('--mes',type=int,default=6,choices=range(1,13),metavar='1..12')
    parser.add_argument('--dia-semana',type=int,default=1,choices=range(7),metavar='0..6')
    parser.add_argument('--estacao',type=int,default=2,choices=range(1,5),metavar='1..4')
    parser.add_argument('--clima',type=int,default=1,choices=range(1,5),metavar='1..4')
    parser.add_argument('--feriado',action='store_true')
    parser.add_argument('--dia-util',action=argparse.BooleanOptionalAction,default=True)
    parser.add_argument('--temperatura',type=float,default=25)
    parser.add_argument('--sensacao',type=float,default=26)
    parser.add_argument('--umidade',type=float,default=50)
    parser.add_argument('--vento',type=float,default=12)
    a=parser.parse_args()
    if not 0 <= a.umidade <= 100 or not -8 <= a.temperatura <= 39 or not 0 <= a.vento <= 67:
        parser.error('Valores fora dos limites da base: umidade 0–100, temperatura -8–39, vento 0–67.')
    print(f'BikeFlow prevê aproximadamente {prever(a)} bicicletas alugadas nessa hora.')
