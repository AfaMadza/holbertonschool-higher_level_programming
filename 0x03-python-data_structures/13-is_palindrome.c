#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to start of linked list.
 * Return: 0 or 1 for True or Fales
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array, list_len, i = 0;

	current = *head;
	if (head == NULL || *head == NULL)
		return (1);
	list_len = 0;
	while (current)
	{
		list_len++;
		current = current->next;
	}
	current = *head;
	array = malloc(list_len * sizeof(int));
	while (current)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	i = 0;
	while (i < list_len / 2)
	{
		if (array[i] != array[list_len - 1 - i])
		{
			free(array);
			return (0);
		}
		i++;
	}
	free(array);
	return (1);
}
