#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to first node of linked list.
 * Return: 0 or 1 for failure or success.
 */
int check_cycle(listint_t *list)
{
	listint_t *future_node, *current;

	if (list == NULL)
		return (0);

	current = list;
	future_node = list->next;
	while (future_node != NULL && future_node->next != NULL)
	{
		if (current == future_node)
			return (1);
		current = current->next;
		future_node = future_node->next->next;
	}
	return (0);
}
