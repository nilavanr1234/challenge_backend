# Challenge 3: Web Scraping Google Search Results

## Objective
Create a script to scrape the top 10 results of a Google search and save the extracted data in JSON format.

## Prerequisites
- Python 3.x
- `requests`, `beautifulsoup4` libraries installed

## Tasks
1. **Script Setup**: Fork and clone the repository. Navigate to `Challenge3` and use `google_search_scrape.py` as your base script.

2. **Implementation**:
   - Modify the parsing function to locate and retrieve the top 10 search results.
   - Extract the title, link, and a brief description for each result.
   - Save the data in `results.json` in the following format:
     ```json
     [
       {
         "title": "Title",
         "link": "URL",
         "details": "Description"
       }
     ]
     ```

3. **Error Handling**:
   - Implement error handling for the request and processing steps.
   - Manage scenarios with fewer than 10 results.

## Submission
- Push your code to your fork and submit the link to your repository.

## Evaluation Criteria
- Correct extraction and saving of data.
- Code readability and structure.
- Effective error and edge case handling.

## Note
- Observe `robots.txt` and legal policies related to web scraping and the use of scraped data.