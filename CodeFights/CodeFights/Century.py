def centuryFromYear(year):
    centuryFromYear = 16;
    solved = 0;
    while (not(solved)):
        if ((centuryFromYear * 100) >= year):
            solved = 1;
        else:
            centuryFromYear += 1;    
    return(centuryFromYear)

print (centuryFromYear(1));
print (centuryFromYear(1905));
print (centuryFromYear(1700));
print (centuryFromYear(1988));
print (centuryFromYear(2000));
print (centuryFromYear(2001));
print (centuryFromYear(2005));
