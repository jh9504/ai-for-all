class BaseGenerator:
    client = None
    async_client = None
    model = None

    def __init__(self):
        pass

    def generate(self, prompt=''):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        response = completion.choices[0].message.content
        return response
