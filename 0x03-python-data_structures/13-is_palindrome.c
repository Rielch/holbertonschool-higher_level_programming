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
        list = malloc(sizeof(int) * ((size / 2) + (size % 2)));
        temp = *head;
        while (temp != NULL)
        {
                temp = temp->next;
                size++;
        }
        list = malloc(sizeof(int) * ((size / 2) + (size % 2)));
        temp = *head;
        while (temp != NULL)
        {
                if (i < ((size / 2) + (size % 2)))
                {
                        list[i] = temp->n;
                }
                else
                {
                        if (list[size - i - 1] != temp->n)
                        {
                                free(list);
                                return (0);
                        }
                }
                temp = temp->next;
                i++;
        }
        free(list);
        return (1);
}
