# 연도별 학급당 학생 수 데이터
data = {
    2021: 23.0,
    2020: 23.4,
    2019: 24.5,
    2018: 26.2,
    2017: 28.2,
    2016: 29.3,
    2015: 30.0,
    2014: 30.9,
    2013: 31.9,
    2012: 32.5,
    2011: 33.1,
    2010: 33.7
}

# 1) 전년도에 비해 가장 급격하게 학생 수가 줄어든 해
def year_of_most_rapid_decline(data):
    max_decline = 0
    decline_year = None
    for year in range(2010, 2021):
        if year + 1 in data:
            decline = data[year] - data[year + 1]
            if decline > max_decline:
                max_decline = decline
                decline_year = year + 1
    return decline_year

# 2) 학급 당 학생 수가 30명 미만으로 떨어진 해
def year_fell_below_30(data):
    for year, students in data.items():
        if students < 30:
            return year
    return None

# 3) 2010년부터 2021년 사이에 평균적으로 학급당 학생 수는 어느 정도 감소했는가
def average_decline_per_year(data):
    years = list(data.keys())
    total_decline = data[years[0]] - data[years[-1]]
    number_of_years = years[-1] - years[0]
    average_decline = total_decline / number_of_years
    return average_decline

# 결과 출력
print("1) 전년도에 비해 가장 급격하게 학생 수가 줄어든 해:", year_of_most_rapid_decline(data))
print("2) 학급 당 학생 수가 30명 미만으로 떨어진 해:", year_fell_below_30(data))
print("3) 2010년부터 2021년 사이에 평균적으로 학급당 학생 수는 어느 정도 감소했는가:", average_decline_per_year(data))
