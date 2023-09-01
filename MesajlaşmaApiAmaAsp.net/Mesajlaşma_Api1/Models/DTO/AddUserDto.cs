using System.ComponentModel.DataAnnotations;

namespace Mesajlaşma_Api1.Models.DTO
{
	public class AddUserDto
	{
		public string Nickname { get; set; }

		public string Password { get; set; }

		[EmailAddress]
		public string MailAddress { get; set; }
	}
}
