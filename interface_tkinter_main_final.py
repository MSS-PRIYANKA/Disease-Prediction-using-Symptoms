import tkinter as tk
from tkinter import filedialog
import joblib
import numpy as np
import openai



def two_functions():
    close_window()
    open_new_window()
    
def close_window():
    window = tk.Toplevel(root)
    root.destroy()

def open_new_window():
    # create new window
    def predict_disease():
        # Get selected symptoms
        selected_symptoms = [X[i] for i in range(len(X)) if options_vars[i].get()]

        # Load trained model
        clf = joblib.load("C:\\Users\\PRIYANKA\\Downloads\\random_forest_model.joblib") 

        # Predict disease
        if len(selected_symptoms) == 0:
            prediction = "No symptoms selected"
        else:
            sample = np.zeros(len(X))
            for i in range(len(X)):
                if X[i] in selected_symptoms:
                    sample[i] = 1
            prediction = clf.predict(np.array(sample).reshape(1, -1))[0]

        # Open new window to display prediction
        
        
        new_window = tk.Toplevel(window)
        new_window.title("Prediction")
        new_window.configure(bg = "#B9F3E4")
        # Display predicted disease
        prediction_label = tk.Label(new_window, text=f"The predicted disease is : {prediction}", font=("Helvetica", 14, "bold"), bg ="#B9F3E4")
        prediction_label.pack(pady=10)
        #Information
        openai.api_key = "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"
        completion = openai.Completion.create(engine = "text-davinci-003", prompt=f'what is {prediction}?', max_tokens = 1000)
        answer = completion.choices[0]['text']
        output_label = tk.Label(new_window, text=answer, wraplength=400, font=("Arial", 13), bg ="#B9F3E4")
        output_label.pack(pady=10)

        # Add close button to close prediction window
        close_button = tk.Button(new_window, text="Close", command=new_window.destroy, bg="#F6E6C2", font=("Helvetica", 12, "bold"), padx=10, pady=5)
        close_button.pack(pady=10)
        
        


    X = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
        'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
        'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
        'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
        'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
        'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
        'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
        'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
        'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
        'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
        'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
        'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']


    window = tk.Tk()
    window.title("Machine Learning Model Interface")
    window.configure(bg="#F3BFB3")
    def uncheck_all():
        for var in options_vars:
            var.set(0)

    # Create a frame to hold checkbox options and scrollbar
    options_frame = tk.Frame(window)
    options_frame.grid(row=0, column=0, sticky="nsew")

    # Create a canvas to hold options frame and scrollbar
    canvas = tk.Canvas(options_frame)
    options_canvas = tk.Frame(canvas)
    scrollbar = tk.Scrollbar(options_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0,0), window=options_canvas, anchor="nw")

    # Create Checkbuttons for each symptom in the options frame
    options_vars = []
    for i in range(len(X)):
        var = tk.BooleanVar()
        options_vars.append(var)
        window.configure(bg = "#F3BFB3")
        tk.Checkbutton(options_canvas, text=X[i], variable=var, font=("Helvetica", 12)).grid(row=i, column=0, sticky="w")

    # Update canvas size and configure scrollbar
    options_canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Button to predict disease
    print_button = tk.Button(window, text="Predict Disease", command=predict_disease, bg="#FFDF7C", font=("Helvetica", 12, "bold"), padx=10, pady=5)

    print_button.grid(row=1, column=0, pady=10)

    # Button to Refresh

    refresh_button = tk.Button(window, text="Refresh", command= uncheck_all, bg="#FFDF7C", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    refresh_button.grid(row=3, column=0, pady=10)
    # Start GUI
    window.mainloop()

root = tk.Tk()

root.title("Project Window")
root.configure(bg="#87CEEB")
root.geometry("1500x1200")
# root.configure()




project_title = tk.Label(root, text="Disease Prediction Based on Symptoms", font=("Roboto", 39, "bold"), bg="#87CEEB", fg="#333333")
project_title.pack(pady=70)

description_label = tk.Label(root, text="People are currently suffering from a variety of diseases. Many people are", font=("Roboto", 17, "bold"), bg="#87CEEB", fg="#333333")
description_label.pack(pady=7)

description_label = tk.Label(root, text="unsure if the symptoms they are experiencing are indicative of a certain disease,", font=("Roboto", 17, "bold"), bg="#87CEEB", fg="#333333")
description_label.pack(pady=7)

description_label = tk.Label(root, text="and hence they are unable to take the required safeguards. For disease", font=("Roboto", 17, "bold"), bg="#87CEEB", fg="#333333")
description_label.pack(pady=7)

description_label = tk.Label(root, text="prediction, the suggested method utilizes Decision trees model.", font=("Roboto", 17, "bold"), bg="#87CEEB", fg="#333333")
description_label.pack(pady=7)

description_label = tk.Label(root, text="The ultimate result will be the mode of all these", font=("Roboto", 17, "bold"), bg="#87CEEB", fg="#333333")
description_label.pack(pady=7)

# add button to main window
button = tk.Button(root, text="Start Project", font=("Roboto", 19), command=two_functions)
button.pack(pady=60)

root.mainloop()