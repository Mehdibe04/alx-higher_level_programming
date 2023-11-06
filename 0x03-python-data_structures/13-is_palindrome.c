#include"lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
    listint_t *curr = *head;
    static listint_t *tp;

    if (curr == NULL)
        return (1);
    if (tp == NULL)
        tp = curr;
    if (is_palindrome(&curr->next) && tp->n == curr->n)
    {
        tp = tp->next;
        return (1);
    }
    else
        return (0);
}
