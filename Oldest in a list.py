#this code is to find the oldest person in a list of the top 5 oldest

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 4) and (nth_person <= 5):
    print('The {}th oldest person lived {} years'.format(nth_person, oldest_people[nth_person-1]))

if (nth_person == 1) and (nth_person <= 5):
    print('The {}st oldest person lived {} years'.format(nth_person, oldest_people[nth_person-1]))

if (nth_person == 2) and (nth_person <= 5):
    print('The {}nd oldest person lived {} years'.format(nth_person, oldest_people[nth_person-1]))

if (nth_person == 3) and (nth_person <= 5):
    print('The {}rd oldest person lived {} years'.format(nth_person, oldest_people[nth_person-1]))