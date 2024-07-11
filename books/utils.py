import hashlib 


def book_id_hash(book_title, publisher):
    combined_data = f"{book_title}| {publisher}"
    combined_data_bytes = combined_data.encode('utf-8')
    hashed_data = hashlib.sha256(combined_data_bytes).hexdigest()
    return hashed_data