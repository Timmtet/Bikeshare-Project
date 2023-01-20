import time
import pandas as pd
import nump as np

# This is a bikeshare project
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #mycode:
    city = input('Hey!!! Welcome. Would you like to see data for chicago, New York City or Washington?\n').lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city = input('Please input one of the following options: Chicago, NewYork or Washington\n')

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may' , 'june', 'all']
    month = input('Which month  would you love to filter by? Is it January, Febuary, March, April, May, June or all\n').lower()
    while month not in months:
        month = input('Please enter the correct month you want to work with. i.e January, Febuary, March, April, May or June\n')

    #if month != 'all':
        #month = months.index(month)+ 1
        #df = df[df['Month']== month]

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Which day of the week would you love to filter by? Is it Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n').lower()
    while day not in days:
        day = input('Please enter a valid day of the week\n')

    #if day != 'all':
        #day = day.index(day) + 1
        #df = df[df['day']== day]



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
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'june', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

# You're still working on bikeshare project

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'febuary', 'march', 'april', 'may', 'june']
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        print('The most common month is: January')
    elif popular_month == 2:
        print('The most common month is: Febuary')
    elif popular_month ==3:
        print('The most common month is: March')
    elif popular_month == 4:
        print('The most common month is: April')
    elif popular_month == 5:
        print('The most common month is: May')
    else:
        print('The most common month is: June')

    #print('The most common month is: ', popular_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_week = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ' , popular_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ' , popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('This is the most popular Start Station: ' , popular_start_station )

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('This is the most popular End Station: ' , popular_end_station)

    # display most frequent combination of start station and end station trip
    df['join'] = df['Start Station'].astype(str) + '-' + ' ' + ' ' + df['End Station'].astype(str)
    print('The most frequent combination is: ' , df['join'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: ' , total_time)


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The total travel time is: ' , mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print('The count of user types is: '  , user_count)

    try:
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('The count of gender is: ' , gender_count)
    except KeyError:
        print('No available data for the selected city')

    try:
        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('The earliest year of birth is: ' , earliest )

        most_recent = df['Birth Year'].max()
        print('The earliest year of birth is: ' , most_recent)

        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ' , most_common)
    except KeyError:
        print('No available data for the selected city')

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
        # Should the user like to see the raw data
        raw_data = input('Would you like to see the first five lines of the raw data\n').lower()

        if raw_data == 'yes':
            print(pd.read_csv(CITY_DATA[city], nrows=5))
        elif raw_data == 'no':
            print("That is okay")
        else:
            raw_data = input('Would you like to see the first five lines of the raw data\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# You just finished working on the bikeshare project
