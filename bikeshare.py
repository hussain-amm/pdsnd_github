import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('which city do you want to use? chicago, new york city or washington? ').lower()
        df=pd.read_csv(CITY_DATA[city])
        
        
        
        


    # TO DO: get user input for month (all, january, february, ... , june)
        month=input('what month do you want as your input?').lower()
        df['month']= df['Start Time']
        if month != 'all':
                    months = ['january','february','march','april','may','june','all']
                    month = months.index(month) + 1
                    df = df[df['month'] == month]
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day=input('what day do you want as your input?').lower()
        days= ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
        df['day_of_week']=df['Start Time']
        day=days.index(day)
        if day != 'all':
            df=df[df['day_of_week'] == day]
            break
            
            
         
            
        
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    while True:
        df=pd.read_csv(CITY_DATA[city])

        df['month']= df['Start Time']
        df['day of week']=df['Start Time']
        df['hour']=df['Start Time']
        break
    return df
    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    
    common_month = df['month'].mode()[0]
    print('most common month: ',common_month)


    # TO DO: display the most common day of week
    
    common_day_of_week = df['day_of_week'].mode()[0]
    print('most common day of the week: ',common_day_of_week)


    # TO DO: display the most common start hour
    
    
    common_start_hour = df['hour'].mode()[0]
    print('most common start hour : ',common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].value_counts()
    print('most common start station is: ',common_start_station)


    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].value_counts()
    print('most common end station is: ',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_station=df[['Start Station','End Station']].mode().loc[0]
    print('most frequent start and end station is:{} an {}'.format(most_frequent_station[0],most_frequent_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('the total travel time is:',total_travel_time)
    


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('the mean travel time is: ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('the type of users are: ',user_types)
    

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders=df['Gender'].value_counts()
        print('the user gender is: ',genders)
    else:
        print('this city does not have gender information')
    
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth=df['Birth Year'].min()
        print('the earliest year of birth is: ',earliest_year_of_birth)
        recent_year_of_birth=df['Birth Year'].max()
        print('the most recent year of birth is: ',recent_year_of_birth)
        common_year_of_birth=df['Birth Year'].mode()[0]
        print('the most common year of birth is: ',common_year_of_birth)
    else:
        print('there is no birth information in this list')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_trip(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[0:4])
        start_loc += 5
        view_desplay = input("Do you wish to continue?: ").lower()
        break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_trip(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
