#include<stdint.h>
#include<memory.h>

int32_t array_sum(int32_t* a, int32_t* b, int32_t* res, int32_t length)
{
    if (a == NULL)
        return -1;
    if (b == NULL)
        return -1;
    if (res == NULL)
        return -1;
    if (length <= 0)
        return length;
    
    int32_t* final_addr = a + length;

    do
    {
        *res = *a + *b;

        a++;
        b++;
        res++;
    } while (a != final_addr);

    return length;
}
