#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to head of list
 *
 * Return: 1 if true, 0 if false
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *current, *next, *prev;
	listint_t *f_half, *s_half, *s_half_temp;

	if (head == NULL || (*head) == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	current = slow;
	next = NULL;
	prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	s_half = prev;
	f_half = *head;
	s_half_temp = s_half;
	while (s_half != NULL)
	{
		if (f_half->n != s_half->n)
		{
			return (0);
		}
		f_half = f_half->next;
		s_half = s_half->next;
	}
	s_half = s_half_temp;
	return (1);
}
