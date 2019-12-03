<p align = "right"> <font size='3'> Adrian Sandoval-Vargas</font></p>
<p align = "right"> <font size='3'>CSI 5810 Assignment 4 </font></p>

<h1></h1>

## Question 1

For this problem I used the language R. I wasn't sure were to find the wine dataset mentioned so I assumed and used the Wine Dataset found in the UCI Machine Learning database.

>
><div style="display:flex">
>     <div style="flex:1;padding-right:5px;">
>          <img src="wine_data_2_3.png">
>     </div>
>     <div style="flex:1;padding-left:5px;">
>          <img src="wine_data_4_5.png">
>     </div>
></div>
>
>Figures of K-means clustering on Wine Dataset.

The SSE and Rand Index are as follows:

||K2|K3|K4|K5|
|--|--|--|--|--|
|SSE|4543801.2|2370742.3|1331953.8|916424.2|
|Rand Index|0.6702850|0.7186568|0.7002476|0.7164984|

## Question 2

Since X1 is our target values, then we do not need X2.
Data:

<img src='Data.png'>

After building the linear model and reading the summary:

``` r
target = CrimeRate$X1
vars = as.matrix(CrimeRate[,3:7])
lm1 <- lm(target ~ vars)
summary(lm1)
```

We obtain:
||Estimate| Std.Error| tvalue| Pr(>abs(t))|
|--|--|--|--|--|
|(Intercept)|  489.649 |   472.366 |  1.037 |0.305592
varsX3|        10.981|      3.078  | 3.568 |0.000884
varsX4|        -6.088 |     6.544 | -0.930 |0.357219
varsX5|         5.480 |    10.053  | 0.545| 0.588428
varsX6|         0.377 |     4.417 |  0.085 |0.932367
varsX7|        5.500 |    13.754 |  0.400 |0.691150

This model gives us something like:

<img src='Rplot.png'>

Using are Intercept and Betas 'Estimates' from our table above. This model gives us:

```math
X1 = 489.65 + (10.98 * X3) - (6.09 * X4) + (5.48 * X5) + (0.38 * X6) + (5.50 * X7)
```

With a Multiple R-squared of: 0.3336 which translates to 33% accuracy. Which is not what we want.

We need to find the best fit line for various attributes using gradient descent.