#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols,glm

# 데이터셋을 팬더스 데이터프레임으로 읽기
wine = pd.read_csv('winequality-both.csv', sep=',', header = 0) # sep = 쉼표, 헤더를 첫번째 행으로 지정
wine.columns = wine.columns.str.replace(' ', '_')
print("가장 첫 5행까지 출력")
print(wine.head())  # 가장 첫 행 출력.

# 변수별 요약 통계 표시
print("변수별 요약 통계")
print(wine.describe())

# 유일값 찾기
print("quality 유일값 찾기")
print(sorted(wine.quality.unique()))

# 빈도 계산
print("quality 유일값 별 빈도계산")
print(wine.quality.value_counts())

# 와인종류에 따른 기술통계 출력
print("와인 종류에 따른 기술통계 출력")
print(wine.groupby('type')[['quality']].describe().unstack('type'))

# 특정 사분위수 계산하기
print("특정 사분위수 계산하기")
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

# 와인 종류에 따른 품질의 분포 확인하기
print("와인 종류에 따른 품질의 분포 확인하기")
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, norm_hist=True, kde = False, color = "red", label = "Red wine"))
print(sns.distplot(white_wine, norm_hist=True, kde = False, color = "white", label = "White wine"))
plt.xlabel('Quality Score')
plt.ylabel('Density')
plt.title('Distribution of Quality by Wine Type')
plt.legend()
plt.show()

# 와인 종류에 따라 품질 차이 검정
print("와인 종류에 따라 품질 차이 검정")
print(wine.groupby('type')[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat : %.3f     pvalue : %.4f' % (tstat,pvalue))

# 모든 변수 쌍 사이의 상관계수 구하기
print("모든 변수 쌍 사이의 상관계수 구하기")
print(wine.corr())

# 변수 간 관계 살펴보기
def take_sample(data_frame, replace = False, n = 200):
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]

reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1.,0.)

print(pd.crosstab(wine.in_sample, wine.type, margins=True))

sns.set_style("dark")

g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci" : False, "x_jitter" : 0.25, "y_jitter" : 0.25}, \
    hue = 'type', diag_kind = 'hist', diag_kws = {"bins" : 10, "alpha" : 1.0}, palette = dict(red = "red", white = "white"),
    markers = ["o", "s"], vars = ['quality', 'alcohol', 'residual_sugar'])

print(g)
plt.suptitle('Hisograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, \
    horizontalalignment = 'center', verticalalignment = 'top', x = 0.5, y = 0.999)
plt.show()

print("\n최소제곱법을 이용한 선형회귀분석\n")
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'

lm = ols(my_formula, data = wine).fit()
# 또는 lm = glm(my_formula, data = wine, family = sm.families.Gaussian()).fit()

print(lm.summary())
print("\nQuantities you can extract from the result : \n%s" % dir(lm))
print("\nCoefficients : \n%s" % lm.params)
print("\nCoefficient Std Errors : \n%s" % lm.bse)
print("\nAdj. R-Squared : \n%.2f" % lm.rsquared_adj)
print("\nF-statistic : %.1f   P-value : %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs : %d    Number of fitted values : %s" % (lm.nobs, len(lm.fittedvalues)))

# 독립변수의 포준화
print("\n독립변수의 표준화\n")
    # 와인 데이터넷의 quality를 종속변수로 생성
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
wine_standardized = pd.concat([dependent_variable, independent_variables_standardized], axis = 1)

lm_standardized = ols(my_formula, data = wine_standardized).fit()
print(lm_standardized.summary())
