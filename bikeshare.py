import time
import pandas as pd
import numpy as np
# add a new comment in master branch
# first change
# second change
# first change
# second change
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
    
    city= str(input('Hi witch city do you want to explore !! chicago ,new york city or washington ? ').lower())
    while city not in ['chicago','new york city','washington']:
        print ("Your choice is invalid. ")
        city=str(input("Please choose one of the following chicago, new york city or washington :").lower())
  
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month= str(input('choose a month (all,january,february, ... , june) :').lower())
    while month not in ['all','january','february','march','april','may', 'june']:
        print ("Your choice is invalid. ")
        month=str(input("Please choose one of the following months (all, january, february, ... , june): ").lower())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= str(input('choose a day (all, monday, tuesday, ... , sunday)').lower())
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']:
        print('your choice is invalid. ')
        day = str(input('Please choose one of the following days (all, monday, tuesday, wednesday, friday, saturday, sunday) : ').lower())


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common Month:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week is: ',common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.time
    common_start_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_Start_Station= df['Start Station'].mode()[0]
    print('Most common Start Station is : ',common_Start_Station)
    # TO DO: display most commonly used end station
    common_End_Station= df['End Station'].mode()[0]
    print('Most common End Station is : ',common_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combi_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(common_combi_station[0], common_combi_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel, 'seconds')
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel,'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n",user_counts)
    # TO DO: Display counts of gender
    if CITY_DATA in ['chicago','new york city']:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n",gender_counts)
    else:
        print('Gender: Oh :( there is no Gender Data to display ')
    # TO DO: Display earliest, most recent, and most common year of birth
    if CITY_DATA in ['chicago','new york city']:
        earliest_by=df['Birth Year'].max()
        most_recent_by=df['Birth Year'].min()
        most_common_by = df['Birth Year'].mode()[0]
        print('earliest Birth Year is {} \n, most recent Birth Year is {} \n, and most common year of birth is {} \n '\
          .format (earliest_by,most_recent_by,most_common_by))
    else:
        print('Birth Year: Oh :( there is no Birth Year Data to display ')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)   
        n=5
        raw_data= input('would you like to display raw data? enter yes or stop :').lower()
        while raw_data == 'yes':
            print(df.head(n))
            n+=5
            raw_data= input('would you like to display more raw data? enter yes or stop :').lower()
            if raw_data == 'yes':
                print(df.head(n))
                n+=5
            elif raw_data == 'stop':
                break
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
    
        
if __name__ == "__main__":
	main()