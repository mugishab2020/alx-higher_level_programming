#include "lists.h"
#include <stddef.h>
/**
 * list_reversing - function to make the copy of the reversed list
 * @head: pointer to the first node i=of the list we are trying to reverse
 * Return: pointer of tthe last node
 */
void list_reversing(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
 * is_palindrome - function to check if the list is a palindrome
 * @head: pointer to the head of the first node
 * Return: 1 if it is  parindrome and 0 if it is not parindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slower = *head, *faster = *head, *tempo = *head, *point = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		faster = faster->next->next;
		if (!faster)
		{
			point = slower->next;
			break;

		}
		if (!faster->next)
		{
			point = slower->next->next;
			break;
		}
		slower = slower->next;
	}

	list_reversing(&point);
	while (point && tempo)
	{
		if (tempo->n == point->n)
		{
			point = point->next;
			tempo = tempo->next;
		}
		else
			return (0);
	}

	if (!point)
		return (1);
	return (0);
}
