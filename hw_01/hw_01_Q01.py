import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import style

from sklearn import datasets

headers = ['age','workclass','fnlwgt','education',
'education-num','marital-status','occupation','relationship'
,'race','sex','capital-gain','captial-loss','hours/week',
'native-country','salary']

data = pd.read_csv("~/Downloads/adult.data", header = None, names = headers )
plt.style.use('dark_background')
#data = data[data["sex"] == ' Male']
#data = data[data["age"] == 22]

#Bargraph prelimiary data
sex = data.sex.unique()
more = data[data["salary"] == " >50K"]
less = data[data["salary"] == " <=50K"]

maleMore = more[more["sex"] == " Male"]
femaleMore = more[more["sex"] == " Female"]
maleLess = less[less["sex"] == " Male"]
femaleLess = less[less["sex"] == " Female"]

'''
#---------Bar Graph stuff------
composite = [len(maleMore.index), len(femaleMore.index)]
composite2 = [len(maleLess.index), len(femaleLess.index)]
#print(len(sex))

#plt.hist(data[1], color = 'g')
#Bargraph male Vs female
plt.figure(figsize=(10, 5))
plt.subplot(131)
plt.bar(sex, composite, color="mediumturquoise", label=">50K")
#labels on bars
for i in range(len(sex)):
    plt.text(x = sex[i], y=composite[i]/2, s = composite[i],size = 6, fontsize=9)
plt.legend()
plt.ylabel('Sample out of ' + str(len(data.index)), fontsize="12")
plt.subplot(133)
plt.bar(sex, composite2, color="mediumvioletred", label="<=50K")
for i in range(len(sex)):
    plt.text(x = sex[i], y=composite2[i]/2, s = composite2[i], size = 6, fontsize=9)

plt.legend()
plt.ylabel('Sample out of ' + str(len(data.index)), fontsize="12")
#plt.title('Male Vs. Female \n>50K')
#plt.xlabel('Sex')
#plt.ylabel('Sample out of ' + str(len(data.index)), fontsize="12")
plt.suptitle("Salary - Male Vs. Female")
#---------End of Bar---------'''
#education = data.education.unique()
#print(education)
'''
#-----------Pie Graph >50K-----------
education = [len(more[more["education"] == " Doctorate"]), 
             len(more[more["education"] == " Masters"]),
             len(more[more["education"] == " Bachelors"]),
             len(more[more["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
             len(more[more["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])])
            ]   

#maledoc = maleMore[maleMore["education"] == " Doctorate"]
#maleMas = maleMore[maleMore["education"] == " Masters"]
#maleBac = maleMore[maleMore["education"] == " Bachelors"]
#maleHS  = maleMore[maleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]
#maleOth = maleMore[maleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])]
#print(maleHS[["education", "sex", "salary"]])

maleFemale = [len(maleMore[maleMore["education"] == " Doctorate"]),
    len(femaleMore[femaleMore["education"]== " Doctorate"]),
    len(maleMore[maleMore["education"] == " Masters"]),
    len(femaleMore[femaleMore["education"]== " Masters"]),
    len(maleMore[maleMore["education"] == " Bachelors"]),
    len(femaleMore[femaleMore["education"]== " Bachelors"]),
    len(maleMore[maleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
    len(femaleMore[femaleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
    len(maleMore[maleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])]),
    len(femaleMore[femaleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])])
]

fig, ax = plt.subplots()
size = 0.3
#vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
#vals = [len(maledoc), len(maleMas), len(maleBac), len(maleHS), len(maleOth)]
outLabels = ['Doctorate', 'Masters', 'Bachelors', '<= High School', 'Other']
innerLabels = [sex[0],sex[1],sex[0],sex[1],sex[0],sex[1],sex[0],sex[1],sex[0],sex[1]]

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(5)*4)
colors = ["mediumturquoise", "mediumvioletred"]
inner_colors = ["mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred", ]


ax.pie(education, labels=outLabels, radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.1f%%', pctdistance=.85)
#ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
 #      wedgeprops=dict(width=size, edgecolor='w'))


ax.pie(maleFemale, radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.1f%%', pctdistance=.80)

pat = [Line2D([0], [0], color = colors[0], label=sex[0]), Line2D([0], [0], color = colors[1], label=sex[1])]
ax.legend(handles = pat, loc = "upper right" )
ax.set(aspect="equal", title='Education of >50K')
fig.savefig("pie_chart_of_>50k.png", format='png')

#------------End Pie Graph----------
'''
'''
#-----------Pie Graph <=50K-----------
education = [len(less[less["education"] == " Doctorate"]), 
             len(less[less["education"] == " Masters"]),
             len(less[less["education"] == " Bachelors"]),
             len(less[less["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
             len(less[less["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])])
            ]   

maleFemale = [len(maleLess[maleLess["education"] == " Doctorate"]),
    len(femaleLess[femaleLess["education"]== " Doctorate"]),
    len(maleLess[maleLess["education"] == " Masters"]),
    len(femaleLess[femaleLess["education"]== " Masters"]),
    len(maleLess[maleLess["education"] == " Bachelors"]),
    len(femaleLess[femaleLess["education"]== " Bachelors"]),
    len(maleLess[maleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
    len(femaleLess[femaleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])]),
    len(maleLess[maleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])]),
    len(femaleLess[femaleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])])
]

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
size = 0.3
#vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
#vals = [len(maledoc), len(maleMas), len(maleBac), len(maleHS), len(maleOth)]
outLabels = ['Doctorate', 'Masters', 'Bachelors', '<= High School', 'Other']
innerLabels = [sex[0],sex[1],sex[0],sex[1],sex[0],sex[1],sex[0],sex[1],sex[0],sex[1]]

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(5)*4)
colors = ["mediumturquoise", "mediumvioletred"]
inner_colors = ["mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred",
                "mediumturquoise", "mediumvioletred", ]


ax.pie(education, labels=outLabels, radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.1f%%', pctdistance=.85)

ax.pie(maleFemale, radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.1f%%', pctdistance=.80)

pat = [Line2D([0], [0], color = colors[0], label=sex[0]), Line2D([0], [0], color = colors[1], label=sex[1])]
ax.legend(handles = pat, loc = "upper right" )
ax.set(aspect="equal", title="Education of <=50K")
fig.savefig("pie_chart_<=50.png", format='png')
#------------End Pie Graph----------
'''
'''
#-----------Scatter Plot >50k Education Vs. Country----------
# Preview Nice
# fig, ax = plt.subplots(2, 2, figsize=(10, 25), sharex=True)
fig, ax = plt.subplots(2, 2, figsize=(16, 16), sharex=True)
country = data["native-country"].unique()
filtered_country = np.delete(country, 4)

vals = []
colors = ['red', 'blue', 'green', 'yellow', 'white', 'cyan', 'purple', 'turquoise', 'mediumspringgreen', 'lime', 'royalblue', 'teal', 'deepskyblue', 'hotpink', 'coral', 'tomato', 'navajowhite',
 'mistyrose', 'lightyellow', 'palegreen', 'silver', 'orchid', 'plum', 'honeydew', 'gold', 'linen', 'lavender', 'darkviolet', 'lightcyan', 'oldlace', 'firebrick', 'slategray', 'grey', 'salmon', 'maroon',
 'orange', 'thistle', 'lawngreen', 'whitesmoke', 'mediumvioletred', 'skyblue', 'khaki']
labels = ['Doctorate', 'Masters', 'Bachelors', '<= High School', 'Other']
pat = []
xLabel = "Degree"
yLabel = "# of Persons"

for i in range(0, len(filtered_country)):
    #USA DATA
    if i == 0:
        #Males
        vals = [len(maleMore[(maleMore["education"] == " Doctorate") & (maleMore["native-country"] == filtered_country[i])]),
            len(maleMore[(maleMore["education"] == " Masters") & (maleMore["native-country"] == filtered_country[i])]),
            len(maleMore[(maleMore["education"] == " Bachelors") & (maleMore["native-country"] == filtered_country[i])]),
            len(maleMore[(maleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (maleMore["native-country"] == filtered_country[i])]),
            len(maleMore[(maleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (maleMore["native-country"] == filtered_country[i])])]
        ax[0, 0].scatter(labels, vals, c = colors[i])
        pat.append(Line2D([0], [0], marker='o', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
        ax[0, 0].set_title("US Born Males >50k", fontsize = 18)
        #ax[0, 0].set(ylabel = yLabel)
        ax[0, 0].set_ylabel(yLabel, fontsize = 16)
        #Females
        vals = [len(femaleMore[(femaleMore["education"] == " Doctorate") & (femaleMore["native-country"] == filtered_country[i])]),
            len(femaleMore[(femaleMore["education"] == " Masters") & (femaleMore["native-country"] == filtered_country[i])]),
            len(femaleMore[(femaleMore["education"] == " Bachelors") & (femaleMore["native-country"] == filtered_country[i])]),
            len(femaleMore[(femaleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (femaleMore["native-country"] == filtered_country[i])]),
            len(femaleMore[(femaleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (femaleMore["native-country"] == filtered_country[i])])]
        ax[0, 1].scatter(labels, vals, c = colors[i], marker='^')
        pat.append(Line2D([0], [0], marker='^', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
        ax[0, 1].set_title("US Born Females >50k", fontsize = 18)
        #ax[0, 1].set( ylabel = yLabel)
        ax[0, 1].set_ylabel(yLabel, fontsize = 16)
    else:    
        #Foreign Males Information
        vals = [len(maleMore[(maleMore["education"] == " Doctorate") & (maleMore["native-country"] == filtered_country[i])]),
                len(maleMore[(maleMore["education"] == " Masters") & (maleMore["native-country"] == filtered_country[i])]),
                len(maleMore[(maleMore["education"] == " Bachelors") & (maleMore["native-country"] == filtered_country[i])]),
                len(maleMore[(maleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (maleMore["native-country"] == filtered_country[i])]),
                len(maleMore[(maleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (maleMore["native-country"] == filtered_country[i])])]
        if np.count_nonzero(vals) > 0:
            #plt.subplot(131)
            #plt.scatter(labels, vals, c = colors[i])
            ax[1, 0].scatter(labels, vals, c = colors[i])
            pat.append(Line2D([0], [0], marker='o', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
            ax[1, 0].set_title("Foreign Born Males >50k", fontsize = 18)
            #ax[1, 0].set(xlabel = xLabel, ylabel = yLabel)
            ax[1, 0].set_xlabel(xLabel, fontsize = 16)
            ax[1, 0].set_ylabel(yLabel, fontsize = 16)
            ax[1, 0].set_xticklabels(labels, rotation=0, fontsize=12)

        #Foreign Females Information
        vals = [len(femaleMore[(femaleMore["education"] == " Doctorate") & (femaleMore["native-country"] == filtered_country[i])]),
                len(femaleMore[(femaleMore["education"] == " Masters") & (femaleMore["native-country"] == filtered_country[i])]),
                len(femaleMore[(femaleMore["education"] == " Bachelors") & (femaleMore["native-country"] == filtered_country[i])]),
                len(femaleMore[(femaleMore["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (femaleMore["native-country"] == filtered_country[i])]),
                len(femaleMore[(femaleMore["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (femaleMore["native-country"] == filtered_country[i])])]
        if np.count_nonzero(vals) > 0:
            ax[1, 1].scatter(labels, vals, c = colors[i], marker='^')
            pat.append(Line2D([0], [0], marker='^', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
            ax[1, 1].set_title("Foreign Born Females >50k", fontsize = 18)
            #ax[1, 1].set(xlabel = xLabel, ylabel = yLabel)
            ax[1, 1].set_xlabel(xLabel, fontsize = 16)
            ax[1, 1].set_ylabel(yLabel, fontsize = 16)
            ax[1, 1].set_xticklabels(labels, rotation=0, fontsize=12)


lgd = ax[0, 1].legend(handles = pat, loc = "best", bbox_to_anchor=(1, 1))
title = fig.suptitle("Education By Country", fontsize= 25, y = .95)

fig.savefig("Foreign_vs_Domestic_>50k.png",format='png', bbox_extra_artists=(lgd, title), bbox_inches='tight')

#-----------End Scatter Plot >50k Education Vs. Country----------
'''
'''
#-----------Scatter Plot <=50k Education Vs. Country----------
# Preview Nice
# fig, ax = plt.subplots(2, 2, figsize=(10, 25), sharex=True)
fig, ax = plt.subplots(2, 2, figsize=(20, 20), sharex=True)
country = data["native-country"].unique()
filtered_country = np.delete(country, 4)

vals = []
colors = ['red', 'blue', 'green', 'yellow', 'white', 'cyan', 'purple', 'turquoise', 'mediumspringgreen', 'lime', 'royalblue', 'teal', 'deepskyblue', 'hotpink', 'coral', 'tomato', 'navajowhite',
 'mistyrose', 'lightyellow', 'palegreen', 'silver', 'orchid', 'plum', 'honeydew', 'gold', 'linen', 'lavender', 'darkviolet', 'lightcyan', 'oldlace', 'firebrick', 'slategray', 'grey', 'salmon', 'maroon',
 'orange', 'thistle', 'lawngreen', 'whitesmoke', 'mediumvioletred', 'skyblue', 'khaki']
labels = ['Doctorate', 'Masters', 'Bachelors', '<= High School', 'Other']
pat = []
xLabel = "Degree"
yLabel = "# of Persons"

for i in range(0, len(filtered_country)):
    #USA DATA
    if i == 0:
        #Males
        vals = [len(maleLess[(maleLess["education"] == " Doctorate") & (maleLess["native-country"] == filtered_country[i])]),
            len(maleLess[(maleLess["education"] == " Masters") & (maleLess["native-country"] == filtered_country[i])]),
            len(maleLess[(maleLess["education"] == " Bachelors") & (maleLess["native-country"] == filtered_country[i])]),
            len(maleLess[(maleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (maleLess["native-country"] == filtered_country[i])]),
            len(maleLess[(maleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (maleLess["native-country"] == filtered_country[i])])]
        ax[0, 0].scatter(labels, vals, c = colors[i])
        pat.append(Line2D([0], [0], marker='o', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
        ax[0, 0].set_title("US Born Males <=50k", fontsize = 18)
        #ax[0, 0].set(ylabel = yLabel)
        ax[0, 0].set_ylabel(yLabel, fontsize = 16)
        #Females
        vals = [len(femaleLess[(femaleLess["education"] == " Doctorate") & (femaleLess["native-country"] == filtered_country[i])]),
            len(femaleLess[(femaleLess["education"] == " Masters") & (femaleLess["native-country"] == filtered_country[i])]),
            len(femaleLess[(femaleLess["education"] == " Bachelors") & (femaleLess["native-country"] == filtered_country[i])]),
            len(femaleLess[(femaleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (femaleLess["native-country"] == filtered_country[i])]),
            len(femaleLess[(femaleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (femaleLess["native-country"] == filtered_country[i])])]
        ax[0, 1].scatter(labels, vals, c = colors[i], marker='^')
        pat.append(Line2D([0], [0], marker='^', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
        ax[0, 1].set_title("US Born Females <=50k", fontsize = 18)
        #ax[0, 1].set( ylabel = yLabel)
        ax[0, 1].set_ylabel(yLabel, fontsize = 16)
    else:    
        #Foreign Males Information
        vals = [len(maleLess[(maleLess["education"] == " Doctorate") & (maleLess["native-country"] == filtered_country[i])]),
                len(maleLess[(maleLess["education"] == " Masters") & (maleLess["native-country"] == filtered_country[i])]),
                len(maleLess[(maleLess["education"] == " Bachelors") & (maleLess["native-country"] == filtered_country[i])]),
                len(maleLess[(maleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (maleLess["native-country"] == filtered_country[i])]),
                len(maleLess[(maleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (maleLess["native-country"] == filtered_country[i])])]
        if np.count_nonzero(vals) > 0:
            #plt.subplot(131)
            #plt.scatter(labels, vals, c = colors[i])
            ax[1, 0].scatter(labels, vals, c = colors[i])
            pat.append(Line2D([0], [0], marker='o', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
            ax[1, 0].set_title("Foreign Born Males <=50k", fontsize = 18)
            #ax[1, 0].set(xlabel = xLabel, ylabel = yLabel)
            ax[1, 0].set_xlabel(xLabel, fontsize = 16)
            ax[1, 0].set_ylabel(yLabel, fontsize = 16)
            ax[1, 0].set_xticklabels(labels, rotation=0, fontsize=12)

        #Foreign Females Information
        vals = [len(femaleLess[(femaleLess["education"] == " Doctorate") & (femaleLess["native-country"] == filtered_country[i])]),
                len(femaleLess[(femaleLess["education"] == " Masters") & (femaleLess["native-country"] == filtered_country[i])]),
                len(femaleLess[(femaleLess["education"] == " Bachelors") & (femaleLess["native-country"] == filtered_country[i])]),
                len(femaleLess[(femaleLess["education"].isin([" HS-grad", " 11th", " 9th", " 7th-8th", " 5th-6th", " 10th", " 1st-4th", " Preschool", " 12th"])) & (femaleLess["native-country"] == filtered_country[i])]),
                len(femaleLess[(femaleLess["education"].isin([' Some-college', ' Assoc-acdm', ' Assoc-voc', ' Prof-school'])) & (femaleLess["native-country"] == filtered_country[i])])]
        if np.count_nonzero(vals) > 0:
            ax[1, 1].scatter(labels, vals, c = colors[i], marker='^')
            pat.append(Line2D([0], [0], marker='^', color='black', label=filtered_country[i] + ", " +str(vals)+"" , markerfacecolor= colors[i], markersize=15))
            ax[1, 1].set_title("Foreign Born Females <=50k", fontsize = 18)
            #ax[1, 1].set(xlabel = xLabel, ylabel = yLabel)
            ax[1, 1].set_xlabel(xLabel, fontsize = 16)
            ax[1, 1].set_ylabel(yLabel, fontsize = 16)
            ax[1, 1].set_xticklabels(labels, rotation=0, fontsize=12)
           


lgd = ax[0, 1].legend(handles = pat, loc = "best", bbox_to_anchor=(1, 1))
title = fig.suptitle("Education By Country", fontsize= 25, y = .92)


fig.savefig("Foreign_vs_Domestic_<=50k.png",format='png', bbox_extra_artists=(lgd, title), bbox_inches='tight')

#-----------End Scatter Plot >50k Education Vs. Country----------

'''