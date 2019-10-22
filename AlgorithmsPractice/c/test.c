#define SIZE 1096

char* fractionToDecimal(int numerator, int denominator) {
    int base[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
    int map[SIZE] = {0};
    char tmp[SIZE];
    int p = 0;
    int sign = (numerator < 0) ^ (denominator < 0);
    long n1 = numerator < 0 ? -((long)numerator) : (long)numerator;
    long n2 = denominator < 0 ? -((long)denominator) : (long)denominator;
    // -------------------------------------------- sign part
    if (sign && numerator) {
        tmp[p++] = '-';
    }
    // -------------------------------------------- integer part 
    long integer = n1 / n2;
    if (integer) {
        int i = 9;
        while (integer / base[i] == 0) {
            i--;
        }
        while (i >= 0) {
            tmp[p++] = integer / base[i] + '0';
            integer %= base[i];
            i--;
        }
    } else {
        tmp[p++] = '0';
    }
    // -------------------------------------------- fraction part 
    long frac = n1 % n2;
    int repeat = 0;
    if (frac) {
        tmp[p++] = '.';
    }
    // loop until frac becomes 0 or same frac appears twice, which means recurring decimal
    while (frac) {  
        int find = 0;
        for (int i = 0; i < p; i++) {
            if (map[i] == frac) {
                find = i;
                break;
            }
        }
        if (find) {
            repeat = find;
            break;
        } else {
            map[p] = frac;  //repeat from here
        }
        tmp[p++] = frac * 10 / n2 + '0';
        frac = (frac * 10) % n2;
    }
    tmp[p] = '\0';
    // -------------------------------------------copy the answer and return
    int returnsize = p;
    if (repeat) {
        returnsize += 2;    // for '(' and ')'
    }
    char *ret = (char *)malloc(sizeof(char) * returnsize);
    
    if (repeat) {
        strncpy(ret, tmp, repeat);
        ret[repeat] = '(';
        strcpy(ret + repeat + 1, tmp + repeat);
        ret[p + 1] = ')';
        ret[p + 2] = '\0';
    } else {
        strcpy(ret, tmp);
    }
    return ret;
}