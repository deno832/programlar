using System.ComponentModel.DataAnnotations;

namespace Mesajlaşma_Api1.Models.Domain
{
	public class User
	{	
		[Key]
		public int Id { get; set; }

		[Required]
		public string Nickname { get; set; }

		[Required]
		public string Password { get; set; }

		[Required]
		[EmailAddress]
		public string MailAddress { get; set; }
		
	}
}
