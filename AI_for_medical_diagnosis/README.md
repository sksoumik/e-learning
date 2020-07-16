
# Week-1

- Instance segmentation: object localization and detect boundaries. 
- Process an chest X-ray image and detect whether it conatains fluids or not. This condition is called Edema. 
- In week 2, learn how to generate heat maps that show that where in the image the model is finding evidence of the disease 

## Chest X-ray classification

- 3 areas where AI is doing tremendously good at medical image diagnosis: Dermatology, Ophthamology(Diabetic ratinopathy), and Histopathology(examination of tissues under the microscope)

## Ungraded lab: EDA

- First step is to explore data
 
 Unique IDs check:

 ```
 print(f"The total patient ids are {train_df['PatientId'].count()}, from those the unique ids are {train_df['PatientId'].value_counts().shape[0]}")
```
<br/>

`value_counts()` function is used to get a Series containing counts of *unique* values.
`
Print out the number of positive labels for each class

```
for column in columns:
    print(f"The class {column} has {train_df[column].sum()} samples")
```
---








