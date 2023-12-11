# Prompt Template to Replace

Here is a general idea about my company's documents:

```
## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 

## Title: 
Content: 


```

I want you to pretend to be a helpful chatbot and guide my employee on the questions they have with my documents.

The question they have is as follows:

**Question**

Reply to this in a JSON format resembling this:

{
    "redirect": ,
    "response": {
      "recommended_document": "",
      "steps": [
            "",
            "",
            "",
            "",
            ""
    ],
      "additional_advice": ""
    }
}

If the question requires a redirect to the URL, se the redirect to true, else set it to false