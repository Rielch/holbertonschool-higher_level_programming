#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in the correct position
 *
 * @head: head of the linked list
 * @number: number to be inserted
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *next, *past;

new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;
new->next = NULL;
if (*head == NULL)
{
*head = new;
return (new);
}
next = *head;
next = next->next;
past = *head;
if (past->n > new->n)
{
*head = new;
new->next = past;
return (new);
}
while (next != NULL)
{
if (new->n > next->n)
{
past = next;
next = next->next;
}
else
{
break;
}
}
past->next = new;
new->next = next;
return (new);
}
