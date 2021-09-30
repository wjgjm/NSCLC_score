# NSCLC_score
1. This file is about the new NSCLC scor that can give you an overview of NSCLC combined with malignant pleural effusions patient's survival at different time points. 
2. To use this model you need:
      1. download all files to the same folder
      2. run model_usage.ipynb file and it will give you your score
      3. please refer to the KM plot in the paper with your score and you can see your survival probability
3. File discriptions
      1. NSCLC_model.pkl ------The model pickle file
      2. test_file.csv  ------- our example file
      3. get_score.py --------- score calculation 
      4. model_usage --------- main program(the file you need to run)
4. Variable decode
      PLEASE KEEP YOUR VARIABLE NAMES AS SAME AS THE TEST FILE. 
      Here is the corresponding names of variable names: [Note: that all categorical variables should be dummy variables just like the test file]
      1. age : your age
      2. race_2: Non-hispanic black  1:yes, 0:no
      3. race_3: Asian, multi-race and hispanic: 1: yes, 0:no
      4. gender_2: Female, 1:yes, 0:no
      5. site_2: if your cancer primary site is middle lobe : 1: yes, 0:no
      6. site_3: if your cancer primary site is lower lobe: 1: yes, 0:no
      7. site_4: if your cancer primary site is main bronchus: 1: yes, 0:no
      8. site_5: if your cancer primary site is not in upper lobe, middle lobe, lower lobe and main bronchus : 1: yes, 0:no
      9. marital_2: if you are divorced: 1: yes, 0:no
      10. marital_3: if you are seperated: 1: yes, 0:no
      11. marital_4: if you are single: 1: yes, 0:no
      12. marital_5: if you are unmarried or Domestic Partner: 1: yes, 0:no
      13. marital_6: if you are widowed : 1: yes, 0:no
      14. N_2: Nstage as N2: 1: yes, 0:no
      15. N_3: Nstage as N3: 1: yes, 0:no
      16. N_4: Nstage as N4: 1: yes, 0:no
      17. M_4: Mstage as M1b : 1: yes, 0:no
      18. surgery_2: if you have done surgery to treat your NSCLC,1:No, 2:Yes
      19. radiation_2: if you have done radiation treatment for your NSCLC, 1:No, 2:Yes
      20. tumorsize_2: if your tumor size ≥3cm and <5cm : 1: yes, 0:no
      21. tumorsize_3: if your tumor size ≥5cm and <7cm: 1: yes, 0:no
      22. tumorsize_4: if your tumor size >7cm : 1: yes, 0:no
