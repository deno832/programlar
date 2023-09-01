using Mesajlaşma_Api1.Data;
using Mesajlaşma_Api1.Models.Domain;
using Mesajlaşma_Api1.Models.DTO;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Mesajlaşma_Api1.Controllers
{
	[Route("api/[controller]")]
	[ApiController]
	public class MessagesController : ControllerBase
	{

		private readonly Mesajlaşma_Api1DbContext dbContext;
		public MessagesController(Mesajlaşma_Api1DbContext dbContext)
		{
			this.dbContext = dbContext;
		}

		[HttpPost]
		[Route("Send_messages")]
		public IActionResult send_msg([FromBody] SendMessageDto sendMessageDto)
		{
			var user = dbContext.Users.FirstOrDefault(u => u.Nickname == sendMessageDto.nickname && u.Password == sendMessageDto.password);

			if (user == null)
			{
				var fail = new
				{
					message = "Invalid credentials!"
				};
				return Unauthorized(fail);
			}

			var message = new Message
			{
				SenderId = user.Id,
				ReceiverId = sendMessageDto.receiver_id,
				MessageText = sendMessageDto.message_content,
				Date = DateTime.Now
			};

			dbContext.Messages.Add(message);
			dbContext.SaveChanges();

			var sucess = new
			{
				message = "Sucess!"
			};

			return Ok(sucess);

		}



		[HttpPost]
		[Route("Get_messages")]
		public IActionResult get_msg([FromBody] GetMsgDto getMsgDto)
		{
			var user = dbContext.Users.FirstOrDefault(u => u.Nickname == getMsgDto.nickname && u.Password == getMsgDto.password);

			if (user == null)
			{
				var fail = new
				{
					message = "Invalid credentials!"
				};
				return Unauthorized(fail);
			}

			var messages = dbContext.Messages.Include(m => m.Receiver)
				.Where(m => (m.SenderId == user.Id && m.ReceiverId == getMsgDto.wanted_person) || (m.SenderId == getMsgDto.wanted_person && m.ReceiverId == user.Id))
				.ToList();


			return Ok(messages);
		}
	}
}
