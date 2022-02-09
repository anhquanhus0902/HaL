### Intro to Recommender Systems

#### What are recommender systems?

Recommenders systems capture the pattern of people's behaviour and use it to predict what else they might want or like.

#### Applications

- What to buy?
  - E-commerce, books, movies, beer, shoes

- Where to eat?

- Which job to apply to?

- Who you should be friends with?
  - LinkedIn, FB, ...

- Personalize your experience on the web
  - News platforms, new personalization

#### Advantages of recommender systems

- Broader exposure
- Possibility of continual usage or purchase of products
- Provides better experience

#### Two types of recommender systems

- Content-Based
  - Content-based systems try to figure out what a user's favorite aspects of an item are, and then make recommendations on items that share those aspects.

- Collaborative Filtering
  - Collaborative filtering techniques find similar groups of users, and provide recommendations based on similar tastes within that group.

#### Implementing recommender systems

- Memory-based
  - Uses the entire user-item dataset to generate a recommendation
  - Uses statistical techniques to approximate users or items

- Model-based
  - Develops a model of users in an attempt to learn their preferences
  - Models can be created using ML techniques like regression, clustering, classification, etc.

### Content-Based Recommender Systems

### Collaborative Filtering

Collaborative filtering has basically two approaches: user-based and item-based.

- User-based collaborative filtering
  - Based on user's neighborhood

- Item-based collaborative filtering
  - Based on item's similarity

#### User-based collaborative filtering

Collaborative filtering basis this similarity on things like history, preference, and choices that users make when buying, watching, or enjoying something.

#### Steps

1. Learning the similarity weights
2. Create the weighted ratings matrix

#### Challenges of collaborative filtering

- Data Sparsity
  - Users in general rate only a limited number of items
- Cold start
  - Difficult in recommendation to new users or new items
- Scalability
  - Increase in number of users or items