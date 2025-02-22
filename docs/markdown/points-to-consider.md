Yes, that’s essentially correct. With a well-designed architecture that enforces proper separation of concerns, the frontend doesn’t need to know whether the backend data is coming from an algorithm-based system or a machine learning-based system. The key is to abstract the data retrieval process behind well-defined interfaces (such as APIs) so that the data provider's internal workings are hidden from the consumer.

### Points to Consider
- **Decoupling:**  
  The frontend interacts with the backend through clearly defined contracts (e.g., RESTful APIs). This means it only needs to know the structure and format of the data, not how that data was produced.
  
- **Flexibility:**  
  Whether recommendations are generated via a rule-based algorithm or a machine learning model, as long as the output adheres to the agreed-upon data format, the frontend can render the information without modifications.

- **Maintenance and Scalability:**  
  Separation of concerns helps in isolating changes. If you decide to switch from one backend approach to another (e.g., moving from a heuristic-based system to a more complex ML model), you can do so without overhauling the entire system—provided the output remains consistent.

- **Potential Caveats:**  
  While the abstraction can mask the underlying complexity, there might be subtle differences in performance or data latency. For example, an ML-based system might require more computational time for generating personalized recommendations, which might necessitate adjustments in how the frontend handles loading states or data caching. However, these are engineering challenges that can be managed at the integration layer.

In summary, proper separation of concerns allows your system to be flexible and maintainable, making the choice between algorithmic or ML approaches mostly a backend concern, as long as the communication contracts remain stable.