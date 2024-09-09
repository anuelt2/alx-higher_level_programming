#include "lists.h"

/**
 * check_cycle - Checks if singly linked list has a cycle in it
 * @list: Pointer to list
 *
 * Return: 0 for no cycle, 1 for cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (!list || !list->next)
	{
		return (0);
	}

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
