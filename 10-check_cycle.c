#include "lists.h"
/**
 * check_cycle - fn to check if the linked list has the cycles
 * @lisst: the list inputed
 *
 * Return: 0 for not having the cycle and 1 for having the cycles
 */
int check_cycle(listint_t *list)
{
	listint_t  *slow = h;
	listint_t *quick = h;

	while (quick != NULL && quick->next != NULL) {
        slow = slow->next;
        quick = quick->next->next;
        if (slow == quick) {
            return 1;
        }
    }

    return 0;
}
}
