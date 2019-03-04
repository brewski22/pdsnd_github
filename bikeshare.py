import time
import pandas as pd

# this really needs to be printed only once and not in every restart
print('Hello! Let\'s explore some US bikeshare data.\n')

def get_city():
    """
    Asks user to specify a city database to load.

    Returns:
        (str) city_file - name of the csv file to analyze

    """

    city_dict = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv', 'c': 'chicago.csv' , 'n': 'new_york_city.csv', 'w': 'washington.csv'}

    city = ''
    city_file = ''
    while city not in city_dict:
        # get user input for city (chicago, new york city, washington)
        city = input('Would you like to see data for Chicago(c), New York(n) or Washington(w) ?\n')
        city = city.lower()
        if city not in city_dict:
            print('Invalid input.\n')

    city_file = city_dict[city]
    return city_file

def get_month():
    """
    Asks user to specify a by which month to filter, if any

    Returns:
        (int) month_select - number of the month to analyze

    """
    month_dict = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5 , 'june': 6, 'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6}
    month = ''
    month_select = 0
    while month not in month_dict:
        # get user input for month (all, january, february, ... , june)
        month = input('Select month filter: All(all), January(jan), February(feb), March(mar), April(apr), May(may), June(jun))\n')
        month = month.lower()
        if month not in month_dict:
            print('Invalid input.\n')

    month_select = month_dict[month]
    return month_select

def get_day():
    """
       Asks user to specify a by which day to filter, if any

       Returns:
           (int) day_select - number of the day to analyze

       """
    day_dict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6, 'mo': 0, 'tu': 1, 'we': 2, 'th': 3, 'fr': 4, 'sa': 5, 'su':6 , 'all': 7}
    day = ''
    day_select = 7
    while day not in day_dict:
        # get user input for month (all, january, february, ... , june)
        day = input('Select day filter: All(all), Monday(mo), Tuesday(tu), Wednesday(we), Thursday(thu), Friday(fr), Saturday(sa) Sunday(su)\n')
        day = day.lower()
        if day not in day_dict:
            print('Invalid input.\n')

    day_select = day_dict[day]
    return day_select

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    most_common_month = month_list[index - 1]
    print('The most common month to travel is {}.'.format(most_common_month))

    # display the most common day of week
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['Start Time'].dt.weekday.mode())
    most_common_day = day_list[index]
    print('The most common weekday to travel is {}.'.format(most_common_day))

    # display the most common start hour
    most_common_hour = int(df['Start Time'].dt.hour.mode())
    print('The most common hour to travel is {}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode().to_string(index = False)
    print('The most common start station is {}.'.format(most_common_start))

    # display most commonly used end station
    most_common_end = df['End Station'].mode().to_string(index = False)
    print('The most common end station is {}.'.format(most_common_end))

    # display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most common trip is {}.'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    average_travel_time = df['Trip Duration'].mean()

    # display total travel time
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    print('The total trip duration is {} year(s) {} day(s) {} hour(s) {} minutes and {} seconds.'.format(year, day, hour, minute, second))

    # display mean travel time
    minute, second = divmod(average_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The average trip duration is {} hour(s) {} minutes and {} seconds.'.format(hour, minute, second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df, current_row):
    """Displays 5 rows of raw data if user chooses to do so."""

    #set display option
    pd.set_option('display.max_columns', 999)

    show_raw_list = ['n']
    show_raw = ''
    # offer user to option display raw data
    while show_raw not in show_raw_list:
        show_raw = input('Would you like to display 5 rows of raw data yes(y) or no(n)?\n')
        show_raw = show_raw.lower()
        if show_raw == 'y' or show_raw == 'yes':
            print(df.iloc[current_row:current_row + 5])
            current_row += 5
        elif show_raw not in show_raw_list and (show_raw != 'y' or show_raw != 'yes'):
            print('Invalid input\n')
        if show_raw == 'n' or show_raw == 'no':
            break

    print('-' * 40)

def user_stats(df):

    try: # this try-except is entered as one of the files doesn't contain gender database
         # and the script would fail at this part
         # wich is avoided by the pass statement without any follow up
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print(user_types)

        # Display counts of gender
        # Display counts of user types
        genders = df['Gender'].value_counts()
        print(genders)

        # Display earliest, most recent, and most common year of birth
        birth_years = df['Birth Year'].value_counts()
        print(birth_years)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        pass #one of the csv files doesn't containt Gender column #progressiveDC


def main():

    try:
        while True:
            # load filter
            filename = get_city()
            month_filter = get_month()
            day_filter = get_day()

            # load data file
            df = pd.read_csv(filename)

            #Format Time columns
            df['Start Time'] = pd.to_datetime(df['Start Time'], errors='ignore')
            df['End Time'] = pd.to_datetime(df['End Time'], errors='ignore')

            # filter by month, only if month value was given (1 - 6)
            if month_filter != 0:
                df = df[df['Start Time'].dt.month == month_filter]

            # filter by day only if day value was given (0 - 6)
            if day_filter >= 0 and day_filter <= 6:
                df = df[df['Start Time'].dt.weekday == day_filter]

            # call individual stat functions
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw(df, 0) # starting line for iloc is 0

            restart = input('\nWould you like to restart? Enter yes(y) or no(n) ?\n')
            if restart.lower() != 'y':
                break
    except:
        pass

if __name__ == "__main__":
    main()
