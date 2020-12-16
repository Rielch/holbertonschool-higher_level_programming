#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome
 *
 * @head: head of the linked list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int *list, size = 0, i = 0;
	listint_t *temp = *head;

	if (*head == NULL)
	{
		return (1);
	}
	while (temp != NULL)
	{
		temp = temp->next;
		size++;
	}
	list = malloc(sizeof(int) * size);
	temp = *head;
	size = 0;
	while (temp != NULL)
	{
		list[size] = temp->n;
		temp = temp->next;
		size++;
	}
	while (i < size)
	{
		if (list[i] != list[size - 1])
		{
			free(list);
			return (0);
		}
		i++;
		size--;
	}
	free(list);
	return (1);
}
