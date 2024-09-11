#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted signly linked list
 * @head: Pointer to head of list
 * @number: Number to be inserted
 *
 * Return: Address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *node;

	current = *head;
	new = NULL;
	node = NULL;

	if (head == NULL)
	{
		return (NULL);
	}
	new = malloc(sizeof(*new));
	if (new == NULL)
	{
		perror("Error");
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current && current->n < number)
		{
			node = current;
			current = current->next;
		}
		node->next = new;
		new->next = current;
	}

	return (new);
}
