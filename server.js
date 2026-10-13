const express = require("express");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();

app.use(express.json());
app.use(express.static("."));

const client = new MongoClient("mongodb://127.0.0.1:27017");

async function start() {
    await client.connect();

    const db = client.db("inventory");
    const products = db.collection("products");

    // Read products
    app.get("/products", async (req, res) => {
        res.json(await products.find().toArray());
    });

    // Add product
    app.post("/products", async (req, res) => {
        await products.insertOne(req.body);
        res.json({ message: "Product added" });
    });

    // Update product
    app.put("/products/:id", async (req, res) => {
        await products.updateOne(
            { _id: new ObjectId(req.params.id) },
            { $set: req.body }
        );
        res.json({ message: "Product updated" });
    });

    // Delete product
    app.delete("/products/:id", async (req, res) => {
        await products.deleteOne({
            _id: new ObjectId(req.params.id)
        });
        res.json({ message: "Product deleted" });
    });

    app.listen(3000, () => {
        console.log("Server running at http://localhost:3000");
    });
}

start().catch(console.error);