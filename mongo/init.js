db = db.getSiblingDB('blog_db');

db.createCollection('posts');

db.posts.insertMany([
    { title: "Article 1", content: "Contenu Docker", author: "Alice" },
    { title: "Article 2", content: "Contenu Compose", author: "Bob" },
    { title: "Article 3", content: "Contenu Mongo", author: "Charlie" },
    { title: "Article 4", content: "Contenu MySQL", author: "Diana" },
    { title: "Article 5", content: "Contenu FastAPI", author: "Eve" }
]);