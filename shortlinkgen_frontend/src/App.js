import React, { useState, useEffect } from 'react';
import './App.css'; // Import your CSS file

function App() {
    const [long_url, setLongurl] = useState("");
    const [short_url, setShorturl] = useState("");
    const [returnLongURL, setReturnLongURL] = useState("");

    const handleGetRequest = () => {
      // Make a GET request to retrieve the data
      fetch("http://127.0.0.1:8000/api/v1/shortlinks/")
          .then((res) => {
              if (!res.ok) {
                  throw new Error('Network response was not ok');
              }
              return res.json();
          })
          .then((data) => {
              console.log(data);
              // Set the state with the retrieved data
              setShorturl(data.short_url);
              setReturnLongURL(data.long_url);
          })
          .catch((error) => {
              console.error('Error fetching data:', error);
          });
  };

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://127.0.0.1:8000/api/v1/shortlinks/", {
            method: "POST",
            body: JSON.stringify({ long_url: long_url }),
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
                setShorturl(data.short_url);
                setReturnLongURL(data.long_url);
                setLongurl("");
            });
    };

    // Call the GET request when the component mounts
    useEffect(() => {
      handleGetRequest();
  }, []); // Empty dependency array to run the effect once on component mount


  return (
    <div className="container">
        <input id="inputtext"
            type="text"
            name="lon_gurl"
            value={long_url}
            onChange={(e) => setLongurl(e.target.value)}
        />
        <button className="btn"
            type="submit"
            onClick={(e) => handleSubmit(e)}
            disabled={!long_url}
        >
            Generate
        </button>

        <div className="url">
            <p>Long URL: {returnLongURL}</p>
            <p
                onClick={() => window.open(returnLongURL)}>
                Short URL: {short_url}
            </p>
        </div>
    </div>
);
}

export default App;
