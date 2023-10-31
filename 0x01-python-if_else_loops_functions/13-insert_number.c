#include "lists.h"

/**
 * insert_node - this function inserts a num into a sortd sngly linkd list
 *
 * @head: double ptr
 * @number: the num to insert
 *
 * Return: @ of d new node, or NULL (Failure)
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr_node, *new_node;

	curr_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (curr_node == NULL || curr_node->n >= number)
	{
		new_node->next = curr_node;
		*head = new_node;
		return (new_node);
	}
	while (curr_node && curr_node->next && curr_node->next->n < number)
		curr_node = curr_node->next;
	new_node->next = curr_node->next;
	curr_node->next = new_node;
	return (new_node);
}
