css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 5%;
}
.chat-message .avatar img {
  max-width: 32px;
  max-height: 32px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 95%;
  padding: 0 1.5rem;
  color: #fff;
  display:flex;
  align-items:center;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/HH4rtZM/bot.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/31xG3fv/person.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''