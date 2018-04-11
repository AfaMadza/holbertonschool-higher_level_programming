#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts a number into a linked (sorted) list
 * @head: double pointer to linked list head
 * @number: number to be inserted
 * Return: pointer to node that was added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *n_node = NULL;
	int list_position;
	unsigned int index = 0;

	if (*head == NULL)
	{
		n_node->next = *head;
		add_nodeint(head, number);
	}
	temp = *head;
	while (temp != NULL)
	{
		index += 1;
		if (number < temp->n)
		{
			list_position = 1;
			break;
		}
		else if (number > temp->n && temp->next == NULL)
		{
				list_position = 3;
				break;
		}
		else
		{
			list_position = 2;
			if ((temp->next)->n > number)
				break;
		}
		temp = temp->next;
	}
	if (list_position == 1)
		add_nodeint(head, number);
	else if (list_position == 2)
		insert_nodeint_at_index(head, index, number);
	else if (list_position == 3)
		add_nodeint_end(head, number);
	return (NULL);
}
/**
 * add_nodeint - adds a node to a linked list at head.
 *@head: double pointer to start of list.
 *@n: int member for node to be added.
 * Return: address of new element.
 */
listint_t *add_nodeint(listint_t **head, int n)
{
	listint_t *temp = malloc(sizeof(listint_t));

	if (temp == NULL)
		return (NULL);
	temp->n = n;
	temp->next = *head;
	*head = temp;

	return (*head);
}
/**
 * insert_nodeint_at_index - inserts a node at given index.
 *@head: pointer to start of list.
 *@idx: index.
 *@n: int member for node to be inserted.
 * Return: sum of data member.
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int i;
	listint_t *new, *aft, *prev, *temp;

	if (head == NULL || idx > num_nodes(*head))
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	temp = *head;
	for (i = 0; i < idx - 1; ++i)
		temp = temp->next;
	prev = temp;
	aft = temp->next;
	prev->next = new;
	new->next = aft;
	return (new);
}
/**
 * num_nodes - counts the number of nodes in a linked list.
 *@head: pointer to linked list.
 *Return: number of nodes.
 */
size_t num_nodes(const listint_t *head)
{
	size_t i = 0;

	while (head != NULL)
	{
		i++;
		head = head->next;
	}
	return (i);
}
