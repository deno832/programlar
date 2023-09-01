namespace Mesajlaşma_Api1.Models.DTO
{
	public class SendMessageDto
	{
        public string nickname { get; set; }
        public string password { get; set; }

        public int receiver_id { get; set; }
        public string message_content { get; set; }
	
	}
}
