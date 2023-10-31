#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
