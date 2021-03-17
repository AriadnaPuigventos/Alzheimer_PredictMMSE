# función de predicción
import json

def cambios_input_datos(X_test):
    """leemos csv y hacer la prediccion"""
    path = "../models/"
    loaded_model_CNN_C_ok = load(open(path + "best_model_CNN_C_opt_RMSprop.sav", "rb"))
    prediction = loaded_model_CNN_C_ok.predict(X_test)
    prediction_df = prediction_df.to_json()
    return prediction_df #prediction
