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
	list = malloc(sizeof(int));
	while (temp != NULL)
	{
		list = realloc(list, sizeof(int) * (size + 1));
		list[size] = temp->n;
		temp = temp->next;
		size++;
	}
	while (i < size / 2)
	{
		if (list[size - i - 1] != list[i])
		{
			free(list);
			return (0);
		}
		i++;
	}
	free(list);
	return (1);
}
