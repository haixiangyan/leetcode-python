class Solution:
    def email_thread(self, emails):
        results = []
        dialogs = {}
        thread_id = 0

        for email in emails:
            # Get info from each email string
            sender, receiver, contents = self.get_email_info(email)
            content_length = len(contents)

            # Make (sender, receiver) as a dialog
            curt_dialog = (sender, receiver)

            if curt_dialog not in dialogs:
                thread_id += 1
                dialogs[curt_dialog] = {
                    thread_id: contents
                }
                results.append([thread_id, content_length])
            else:
                # Get previous contents
                prev_contents = contents[1:]
                prev_dialog = dialogs[curt_dialog]
                found = False

                for (prev_thread_id, old_contents) in prev_dialog.items():
                    if old_contents == prev_contents:
                        found = True
                        prev_dialog[prev_thread_id] = contents
                        results.append([prev_thread_id, content_length])
                        break

                # If not found, create new thread
                if not found:
                    thread_id += 1
                    dialogs[thread_id] = contents
                    results.append([thread_id, content_length])

        return results

    def get_email_info(self, email):
        sender, receiver, contents_str = email.split(', ')

        # Switch sender and receiver according the letter order
        if sender > receiver:
            sender, receiver = receiver, sender

        contents = contents_str.split('---')

        return sender, receiver, contents

s = Solution()
emails = ['a@gmail.com, b@gmail.com, abc', 'b@gmail.com, a@gmail.com, cde---abc']
print(s.email_thread(emails))
