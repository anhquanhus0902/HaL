int firstFitSearch(int k)
{	int i, j;

	for (i=0; i<=MAXPAGES-k; i++) {
		for (j=0; j<k; j++) 
			if (getBit(i+j)) break;	
		if (j==k) break;
	}
	if (i<=MAXPAGES-k) return i;
	else return -1;
}

int worstFitSearch(int k)
{	int i, j, count, maxCount = 0, pos = -1;

	for (i=0; i<=MAXPAGES-k; i++) {
		count = 0;
		while ( (i+count<MAXPAGES) && (!getBit(i+count)) ) count++;
		if ( (count>=k)&&(count > maxCount) ) { 
			maxCount = count; 
			pos = i; 
		}
		i += count;
	}
	return (pos);
}

int firstFitSearch(linkList_t *pList, int pages)
{
	if (pList == NULL) return (-1);
	pList->pCurrentNode = pList->pFirstNode;
	while (pList->pCurrentNode != NULL) {
		if ( (pList->pCurrentNode->label=='H')&&
			(pList->pCurrentNode->numPages >= pages)) break;
		pList->pCurrentNode = pList->pCurrentNode->pNext;
	}
	if (pList->pCurrentNode == NULL) return (-2); // memory is full
	else return 0;
}

int worstFitSearch(linkList_t *pList, int pages)
{	linkListNode_t* pNode=NULL;
	int maxPages = 0;

	// write your code here
	if (pList == NULL) return (-1);
	pList->pCurrentNode = pList->pFirstNode;
	while (pList->pCurrentNode != NULL) {
		if ( (pList->pCurrentNode->label=='H')&&
			(pList->pCurrentNode->numPages >= pages)&&
			(pList->pCurrentNode->numPages > maxPages) ) {
			maxPages = pList->pCurrentNode->numPages;
			pNode = pList->pCurrentNode;	// remember the position found
		}
		pList->pCurrentNode = pList->pCurrentNode->pNext;
	}
	if (pNode != NULL) {
		pList->pCurrentNode = pNode;  // set current node to the min node found
		return 0;
	}
	else return (-2); // memory is full
}
