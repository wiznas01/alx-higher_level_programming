#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
/**
 * insert_node - function to insert number in a sorted singly list
 * @head: pointer to head
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new;
		new->next = current;
	}
	return (new);
}
