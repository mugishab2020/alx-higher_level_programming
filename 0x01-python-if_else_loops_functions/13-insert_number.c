#include "lists.h"
/**
 * insert_node - functionn to add the new node on the linkedlist
 * @head: the pointer to the head if the list
 * @number: The data the node will contain
 * Return: Failing status if fails
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_new = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node_new == NULL || node_new->n >= number)
	{
		new->next = node_new;
		*head = new;
		return (new);
	}

	while (node_new && node_new->next && node_new->next->n < number)
		node_new = node_new->next;

	new->next = node_new->next;
	node_new->next = new;

	return (new);
}
