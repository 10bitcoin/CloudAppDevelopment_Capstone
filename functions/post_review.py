# IBM Cloud-specific imports
from cloudant.client import Cloudant
from cloudant.error import CloudantException


# main() will be run automatically when this action is invoked in IBM Cloud
def main(dict):
    """
    Posts a review to the external Cloudant database

    :param dict: Cloud Functions actions accept a single parameter, which must be a JSON object.
                In this case, the param must be an a JSON object with the key "review" with the review data as value.
                I.e: {
                      "review": 
                                {
                                    "id": 1114,        
                                    "name": "Upkar Lidder",
                                    "dealership": 15,
                                    "review": "Great service!",
                                    "purchase": false,
                                    "another": "field",
                                    "purchase_date": "02/16/2021",
                                    "car_make": "Audi",
                                    "car_model": "Car",
                                    "car_year": 2021
                                }
                    }
                The "id" parameter is the id of the review.
    :return: The action returns a JSON object consisting of the HTTP response, which should contain a success message with code 200
             or an error message with code 500.
    """
    
    secret = {
    "COUCH_URL": "https://e33765a3-37fa-4f08-8109-03a9a2aa591b-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "8VxodD5ZTFn7y1yUSOF8XWm3Q3MjTQU4vfrUSXNlnWL-",
    "COUCH_USERNAME": "ae33765a3-37fa-4f08-8109-03a9a2aa591b-bluemix"
    };

    client = Cloudant.iam(
        account_name=secret["ACCOUNT_NAME"], 
        api_key=secret["IAM_API_KEY"],
        url=secret["URL"],
        connect=True, 
    )
    
    db = client["reviews"]
    new_review = db.create_document(dict["review"])   
    
    if new_review.exists():
        result = {
            "headers": {"Content-Type": "application/json"},
            "body": {"message": "Review posted successfully."}
        }
    
        print(new_review)
        return result
        
    else: 
        error_json = {
            "statusCode": 500,
            "message": "Could not post review due to server error."
        }
        return error_json