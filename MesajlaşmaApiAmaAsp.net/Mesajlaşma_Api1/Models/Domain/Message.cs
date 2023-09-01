using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;

namespace Mesajlaşma_Api1.Models.Domain
{
	public class Message
	{
		[Key]
		public int Id { get; set; }

		[Required]
		public int SenderId { get; set; }

		[Required]
		public int ReceiverId { get; set; }

		[Required]
		public string MessageText { get; set; }

		[Required]
		public DateTime Date { get; set; }

		[ForeignKey("SenderId")]
		public User Sender { get; set; }

		[ForeignKey("ReceiverId")]
		public User Receiver { get; set; }


	}
}
