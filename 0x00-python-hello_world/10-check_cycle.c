#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if a list has a cycle
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;
	int found = 0;

	while ((turtle && hare) && hare->next)
	{
		turtle = turtle->next;

		if (hare->next || hare->next->next)
			hare = hare->next->next;
		else
			break;

		if (turtle == hare)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
